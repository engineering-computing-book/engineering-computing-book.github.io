import yaml
import argparse
import glob
import click
import os
from os.path import exists
import shutil
import filecmp
import shutil
import pathlib

page_layout = 'page'

with open('common/book-defs.json') as f:
    book_defs = yaml.safe_load(f)

book = {}
for ed,details in book_defs['editions'].items():
    if exists(details['json-file-cleaned']):
        with open(details['json-file-cleaned']) as f:
            book[ed] = yaml.safe_load(f)
print(details['json-file-cleaned'])
path_base = 'pages/autogenerated/'
paths = {}
path_list_new = []
nonapocryphal_hashes = []
# add sections from an edition
for ed,tbl in book.items():
    for h,data in tbl.items():
        if isinstance(data,dict):
            if 'hash' in data:
                nonapocryphal_hashes.append(h)
                path = path_base + h
                if data['type']=='chapter' or data['type']=='appendix' or data['type']=='section' or data['type']=='subsection' or data['type']=='lab' or data['type']=='resource' or data['type']=='exturl':
                    data['index_path'] = path + "/index.md"
                    path_list_new.append(data['index_path'])
                    data['layout'] = page_layout
                    data['source_reso'] = f"common/online-resources-editable/{data['hash']}/source.md"
                    paths[path] = data # this will overwrite some values when there are multiple editions, but we're only going to use the hash and id
                else:
                    continue

# add apocryphal sections
versioned_hash_dirs = glob.glob('common/versioned/*',recursive=False)
versioned_hashes = list(map(lambda x: x.replace('common/versioned/','',1),versioned_hash_dirs))
apocryphal_hashes = list(set(versioned_hashes) - set(nonapocryphal_hashes))
apocryphal_hashes = [h for h in apocryphal_hashes if not 'lead-in' in h]

# generate online resource source (manually editable) if it doesn't already exist
for path, data in paths.items():
    if not exists(data['source_reso']): # otherwise don't touch it
        os.makedirs(os.path.dirname(data['source_reso']), exist_ok=True)
        with open(data['source_reso'],'w') as f:
            f.write('\nNo online resources.\n')

# generate regular pages

def online_resourcer(data):
    number = f'Section {data["sec"]}'
    title = f'Online Resources for {number}'
    iden = pathlib.PurePath(data['id'])
    iden = iden.name
    if iden:
        iden = '#'+iden+'-online-resources'
    else:
        iden = '#online-resources'
    resources_editable = f"\n{{% include {data['source_reso']} %}}\n"
    return f'\n\n## {title}\n{resources_editable}'

path_list_old = glob.glob('pages/autogenerated/**/index.md',recursive=True)
path_list_stale = [x for x in path_list_old if x not in path_list_new and x not in ['pages/autogenerated/0000/index.md']]
for file in path_list_stale:
    print('deleting file: '+file+' ...')
    if os.path.exists(file):
        shutil.rmtree(os.path.dirname(file))
    else:
        print(" ... but the file does not exist!")

with open("_template.md") as f:
    template = f.read()
with open("_template-external-url.md") as f:
    external = f.read()

for path, data in paths.items():
    index_path = data['index_path']
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    if data['type']=='exturl':
        if not data['url'] == book_defs['editions']['0']['url-companion'] and not data['url'] == book_defs['editions']['0']['url-companion']: # skip if it's a url to this site
            with open(index_path, 'w') as f:
                f.write(external.format(path=path, **data))
    else:
        data['siteurl'] = book_defs['editions']['0']['url-companion']
        with open(index_path+'_tmp', 'w') as f:
            f.write(template.format(path=path, **data))
        with open(index_path+'_tmp', 'a') as f:
            fname = "_includes/common/"+data['hash']+"/index.html"
            fauxname = "_includes/faux/"+data['hash']+"/index.html"
            if os.path.isfile(fname):
                f.write("\n{% include common/"+data['hash']+"/index.html %}")
                f.write(online_resourcer(data))
            else:
                f.write("\n{% include faux/"+data['hash']+"/index.html %}")
        if os.path.isfile(index_path):
            comp = filecmp.cmp(index_path, index_path+'_tmp', shallow = False)
            if not comp:
                print(f'- overwriting: {index_path}')
                os.replace(index_path+'_tmp',index_path)
            else:
                os.remove(index_path+'_tmp')
        else:
            print(f'- creating: {index_path}')
            os.rename(index_path+'_tmp',index_path)

# generate home/index page
with open("_template-homepage.md") as f:
    template = f.read()
data = {}
data['id'] = ''
data['hash'] = '0000'
data['layout'] = page_layout
path = path_base # + data['hash']
home_path = path + "index.md"
os.makedirs(os.path.dirname(home_path), exist_ok=True)
with open(home_path+'_tmp', 'w') as f:
    f.write(template.format(path=path, **data))
with open(home_path+'_tmp', 'a') as f:
    fauxname = "_includes/faux/"+data['hash']+"/index.html"
    f.write("\n\n{% include faux/"+data['hash']+"/index.html %}")
if os.path.isfile(home_path):
    comp = filecmp.cmp(home_path, home_path+'_tmp', shallow = False)
    if not comp:
        print(f'- overwriting: {home_path}')
        os.replace(home_path+'_tmp',home_path)
    else:
        os.remove(home_path+'_tmp')
else:
    print(f'- creating: {home_path}')
    os.rename(home_path+'_tmp',home_path)

# generate apocryphal pages
with open("_template-apocrypha.md") as f:
    template = f.read()
data = {}
data['id'] = ''
data['layout'] = page_layout
for h in apocryphal_hashes:
    data['hash'] = h
    path = path_base + data['hash']
    home_path = path + "/index.md"
    os.makedirs(os.path.dirname(home_path), exist_ok=True)
    with open(home_path+'_tmp', 'w') as f:
        f.write(template.format(path=path, **data))
    with open(home_path+'_tmp', 'a') as f:
        fname = "_includes/common/"+data['hash']+"/index.html"
        f.write("\n{% include common/"+data['hash']+"/index.html %}")
    if os.path.isfile(home_path):
        comp = filecmp.cmp(home_path, home_path+'_tmp', shallow = False)
        if not comp:
            print(f'- overwriting: {home_path}')
            os.replace(home_path+'_tmp',home_path)
        else:
            os.remove(home_path+'_tmp')
    else:
        print(f'- creating: {home_path}')
        os.rename(home_path+'_tmp',home_path)


exit(0)