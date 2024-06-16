
import frida 
import time
import sys

device = frida.get_usb_device()
pid = device.spawn("com.revo.evabs") 
device.resume (pid)

session = device.attach(pid)

hook_script = """
Java.perform(function () {
    console.log("Inside the hook");
    var intent = Java.use("android.content.Intent");
    intent.putExtra.overload("java.lang.String", "java.lang.String").implementation = function(var_1, var_2) {
        console.log("Flag: " + var_2)
    };

});
"""

script = session.create_script(hook_script)
script.load()
sys.stdin.read()

