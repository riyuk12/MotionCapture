import bpy
import pickle


with open(r"C:\Users\user\Desktop\data.dat","rb") as file:
    data=pickle.load(file)


cube=[bpy.context.scene.objects["Cube"],bpy.context.scene.objects["Cube.001"],bpy.context.scene.objects["Cube.002"],bpy.context.scene.objects["Cube.003"],bpy.context.scene.objects["Cube.004"],bpy.context.scene.objects["Cube.005"],bpy.context.scene.objects["Cube.006"],bpy.context.scene.objects["Cube.007"],bpy.context.scene.objects["Cube.008"],bpy.context.scene.objects["Cube.009"],bpy.context.scene.objects["Cube.010"],bpy.context.scene.objects["Cube.011"],bpy.context.scene.objects["Cube.012"]]

for j in range(len(cube)):
    cube[j].keyframe_insert(data_path="location", frame=0)
#cube.keyframe_insert(data_path="location", frame=1)

for i in data.keys():
    if i%1==0:
        posedat=data[i]
        cube[0].location=posedat[0][:]
        cube[1].location=posedat[11][:]
        cube[2].location=posedat[12][:]
        cube[3].location=posedat[13][:]
        cube[4].location=posedat[14][:]
        cube[5].location=posedat[15][:]
        cube[6].location=posedat[16][:]
        cube[7].location=posedat[23][:]
        cube[8].location=posedat[24][:]
        cube[9].location=posedat[25][:]
        cube[10].location=posedat[26][:]
        cube[11].location=posedat[27][:]
        cube[12].location=posedat[28][:]
        for j in range(len(cube)):
            cube[j].keyframe_insert(data_path="location", frame=i)        