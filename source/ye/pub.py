import sys

sys.path.append("../")
import engcom.engcom as engcom

pub = engcom.Publication(
    "solution.py", title="Problem YE", author="Rico Picone"
)
pub.write(to="docx")
