
function hide_class(aclass) {
	var to_hide = document.getElementsByClassName(aclass); // array
	for(var i = 0; i < to_hide.length; i++){
		to_hide[i].classList.add("hide");
	}
}

function unhide_class(aclass) {
	var to_hide = document.getElementsByClassName(aclass); // array
	for(var i = 0; i < to_hide.length; i++){
		to_hide[i].classList.remove("hide");
	}
}

function hide_all() {
	var to_hide = document.querySelectorAll("section.ts:not(.hide),section.ds:not(.hide)")
	for(var i = 0; i < to_hide.length; i++){
		to_hide[i].classList.add("hide");
	}
}

let params = new URLSearchParams(window.location.search)

function get_v_urlparams() {
	return {ts:params.get("TS"),ds:params.get("DS")};
}

function set_v_ts_menu(ts) {
	const menu = document.getElementById("tsmenu");
	menu.innerHTML = ts+"▾";
	document.querySelectorAll(".dropdown.tsd a").forEach(function(element) {
	    if (element.id == 'mi'+ts) {
	    	element.style.fontWeight = 'bold';
	    } else {
		    element.style.fontWeight = 'normal';
		}
	});
}

function set_v_ds_menu(ds) {
	const menu = document.getElementById("dsmenu");
	menu.innerHTML = ds+"▾";
	document.querySelectorAll(".dropdown.dsd a").forEach(function(element) {
	    if (element.id == 'mi'+ds) {
	    	element.style.fontWeight = 'bold';
	    } else {
		    element.style.fontWeight = 'normal';
		}
	});
}

function set_v_ts_tags(ts) {
	document.querySelectorAll(".ts-tag").forEach(function(element) {
    	element.innerHTML = ts;
    });
}

function set_v_ds_tags(ds) {
	document.querySelectorAll(".ds-tag").forEach(function(element) {
    	element.innerHTML = ds;
    });
}

function set_v_ts(ts) {
	ts_old = params.get("TS")
	if (ts == ts_old) {
		params.set("TS","");
		set_v_ts_menu('TX');
		set_v_ts_tags('TX');
		v_filter_page({ts:null,ds:params.get('DS')});
	} else {
		params.set("TS",ts);
		set_v_ts_menu(ts);
		set_v_ts_tags(ts);
		v_filter_page({ts:ts,ds:null});
	}
	history.replaceState(null, null, "?" + params.toString());
}

function set_v_ds(ds) {
	ds_old = params.get("DS")
	if (ds == ds_old) {
		params.set("DS","");
		set_v_ds_menu('DX');
		set_v_ds_tags('DX');
		v_filter_page({ts:params.get('TS'),ds:null});
	} else {
		params.set("DS",ds);
		set_v_ds_menu(ds);
		set_v_ds_tags(ds);
		v_filter_page({ts:null,ds:ds});
	}
	history.replaceState(null, null, "?" + params.toString());
}

function set_v_urlparams(v_dict) {
	if (v_dict.ts !== null) {
		params.set("TS",v_dict.ts);
	}
	if (v_dict.ds !== null) {
		params.set("DS",v_dict.ds);
	}
	history.replaceState(null, null, "?" + params.toString());
	v_filter_page(v_dict);
}

let v_default = {ts:"T1",ds:null};
let v_urlparams = get_v_urlparams();
v_filter_page(v_urlparams);
span_populate(v_urlparams);

function v_filter_page(v_dict) {
	ts = v_dict.ts;
	if (ts) {
		tsp = ts.replace(/\./g,"-"); // use for classes
	} else {
		tsp = null;
	}
	ds = v_dict.ds;
	if (ds) {
		dsp = ds.replace(/\./g,"-"); // use for classes
	} else {
		dsp = null;
	}
	if (!ts && !ds) {
		console.log('setting to default:',v_default);
		set_v_urlparams(v_default);
		set_v_ts_menu(v_default.ts);
		set_v_ts_tags(v_default.ts);
		return
	}
	hide_all();
	if (ts && !ds) {
		set_v_ts_menu(ts);
		set_v_ts_tags(ts);
		document.querySelectorAll("section.ts."+tsp).forEach(function(element) {
		    element.classList.remove("hide");
		});
		document.querySelectorAll("section:not(.ts)").forEach(function(element) {
		    element.classList.remove("hide");
		});
	} else if (!ts && ds) {
		set_v_ds_menu(ds);
		set_v_ds_tags(ds);
		document.querySelectorAll("section.ds."+dsp).forEach(function(element) {
		    element.classList.remove("hide");
		});
		document.querySelectorAll("section:not(.ds)").forEach(function(element) {
		    element.classList.remove("hide");
		});
	} else {
		set_v_ts_menu(ts);
		set_v_ds_menu(ds);
		set_v_ts_tags(ts);
		set_v_ds_tags(ds);
		// TODO test for compatibility of requested versions
		document.querySelectorAll("section.ds."+dsp+",section.ts."+tsp).forEach(function(element) {
		    element.classList.remove("hide");
		});
	}
}

// populate TS and DS spans
function span_populate(v_urlparams) {
	document.querySelectorAll("span.ts").forEach(function(element) {
	    element.textContent = v_urlparams.ts;
	});
	if (!v_urlparams.ds) {
		v_urlparams.ds = "DY"
	}
	document.querySelectorAll("span.ds").forEach(function(element) {
	    element.textContent = v_urlparams.ds;
	});
}