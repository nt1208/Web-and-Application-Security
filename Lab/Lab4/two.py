import frida 
import time
import sys

device = frida.get_usb_device()
pid = device.spawn("com.hellocmu.picoctf") 
device.resume (pid)

session = device.attach(pid)

hook_script = """
Java.perform(function () {
    console.log("Inside the hook");
    var FlagstaffHill = Java.use('com.hellocmu.picoctf.FlagstaffHill');
    FlagstaffHill.getFlag.implementation = function(var_1, var_2) {
        return var_2.getString(2131427375);
    };

});
"""
script = session.create_script(hook_script)
script.load()
sys.stdin.read()