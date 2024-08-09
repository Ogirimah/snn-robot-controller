# from time import sleep
# from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# client = RemoteAPIClient()
# sim = client.require('sim')
# sensor1Handle = sim.getObject('/PioneerP3DX/front_vision_sensor')
# sensor2Handle = sim.getObject('/PioneerP3DX/Vision_sensor')

# sim.startSimulation()
# while sim.getSimulationTime() < 10:
#     image, resolution = sim.getVisionSensorImg(sensor1Handle)
#     sim.setVisionSensorImg(sensor2Handle, image)
#     sleep(0.01)
# sim.stopSimulation()


from coppeliasim_zmqremoteapi_client import RemoteAPIClient
from time import sleep
import datetime
import os
# import cv2


# def save_images_with_datetime(image_dir, save_dir='processed_images'):
# def save_images_with_datetime(img, sensor, save_dir):
#     """Saves images from a directory with datetime-based filenames.

#     Args:
#         image_dir (str): Path to the directory containing input images.
#         save_dir (str): Directory to save the output images.
#     """

#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)

#     now = datetime.datetime.now()
#     filename = now.strftime("%Y-%m-%d_%H-%M-%S") + "_" + sensor
#     output_path = os.path.join(save_dir, filename)
    
#     cv2.imwrite(output_path, img)

    # for filename in os.listdir(image_dir):
    #     if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust for other formats if needed
    #         img_path = os.path.join(image_dir, filename)
    #         img = cv2.imread(img_path)

    #         if img is None:
    #             print(f"Error reading image: {img_path}")
    #             continue

    #         # Get current datetime
    #         now = datetime.datetime.now()
    #         filename = now.strftime("%Y-%m-%d_%H-%M-%S") + "_" + filename
    #         output_path = os.path.join(save_dir, filename)

    #         cv2.imwrite(output_path, img)



client = RemoteAPIClient()
sim = client.require('sim')

# Load scene using the full file path
#TODO
# #Find a way to accomplish this with absolute path
# absolute_path = "C:/Program Files/CoppeliaRobotics/CoppeliaSimEdu/scenes/Scene2.ttt"
# relative_path = sim.getStringParam(sim.stringparam_scenedefaultdir) + '/Scene2.ttt'
# # relative_path = "./Scene2.ttt"
# sim.loadScene(relative_path)

# Changes to enable script run on any machine
cwd = os.getcwd()
scene_path = os.path.join(cwd, 'Scene2.ttt')
print(scene_path)

sim.loadScene(scene_path)

#Get the robot object
robot = sim.getObject('/Pioneer*')

#Display the robots alias
print(sim.getObjectAlias(robot))

#Get and assign the motor handles to variables.
left = sim.getObject("/PioneerP3DX/leftMotor")
right = sim.getObject("/PioneerP3DX/rightMotor")

print(sim.getObjectAlias(left))
print(sim.getObjectAlias(right))

# Get the vision sensor images
training_sensor = sim.getObject("/PioneerP3DX/front_vision_sensor")
feedback_sensor = sim.getObject("/PioneerP3DX/base_sensor")

print(sim.getObjectAlias(training_sensor))
print(sim.getObjectAlias(feedback_sensor))

sim.startSimulation()
while sim.getSimulationTime() < 30:
    image, resolution = sim.getVisionSensorImg(training_sensor, 1) # option of 1(bit0 set) makes the returned image grescale
    # print(resolution)
    # save_images_with_datetime(image, "training", 'training_folder')
    image, resolution = sim.getVisionSensorImg(feedback_sensor, 1) # option 2(bit1 set), imahe is RGBA, option of 0 = RGB
    # print(resolution)
    # save_images_with_datetime(image, "feedback", 'feedback_folder')

    # Set the target velocity to 2
    sim.setJointTargetVelocity(right, 1)
    sim.setJointTargetVelocity(left, 2)


    sleep(0.01)
    simTime = sim.getSimulationTime()
sim.stopSimulation()

# The total-time spent in simulation
totalSimTime = simTime

print("Simulation ended")
