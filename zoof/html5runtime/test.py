from zoof.html5runtime import launch

icondir = r'C:\almar\iep\iep\resources\appicons/'
#icondir = '/home/almar/projects/pyapps/iep/default/iep/resources/appicons/'

# target = 'file:///home/almar/projects/pylib/zoof/zoof/exp/learn_html5.html'
target = "http://helloracer.com/webgl/"

rt1 = launch(target, 'xul', title='my xul app', icon=icondir+'ieplogo64.png')
#rt2 = launch('http://zoof.io')