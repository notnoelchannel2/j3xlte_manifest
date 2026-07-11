import os
path = os.path.expanduser('~/TWRP/frameworks/base/core/jni/android_media_AudioSystem.cpp')
          
with open(path, 'r') as f:
    data = f.read()
# 1. Cleanly disable the missing return warning for this file
data = '#pragma GCC diagnostic ignored \"-Wreturn-type\"\n' + data
data = data.replace('AudioSystem::GetAudioData(par,len,(void *)buffer)', '0')
data = data.replace('AudioSystem::SetEMParameter ((void *)EMParameter, len)', '0')
data = data.replace('AudioSystem::SetAudioData (par,len,(void *)AudioCustomVolumeParameter)', '0')
data = data.replace('AudioSystem::SetAudioCommand(para1, para2)', '0')
data = data.replace('AudioSystem::GetAudioCommand(para1, &ret)', '0')
data = data.replace('AudioSystem::GetEMParameter ((void *)buffer, len)', '0')
with open(path, 'w') as f:
    f.write(data)
