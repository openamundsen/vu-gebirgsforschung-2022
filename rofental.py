import os
os.chdir("D:/setup_tirol/openamundsen-main")
import openamundsen as oa

config = oa.read_config('rofental/rofental.yml')
model = oa.OpenAmundsen(config)
model.initialize()
model.run()
