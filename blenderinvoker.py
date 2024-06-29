import subprocess

# Update the Blender path for macOS
blenderPath = "/Applications/Blender.app/Contents/MacOS/Blender"
projectPath = "../blenderfiles/humanproject.blend"  # Adjust this path if needed
scriptPath = "bodyEditor.py"  # Adjust this path if needed


def run_blender(blenderPath, projectPath, scriptPath, measures):
    subprocess.run([blenderPath,
                    projectPath,
                    '--background',
                    '--python', scriptPath,
                    '--', measures['head'], measures['torso'], measures['legs'], measures['calves'],
                    measures['shoulders'], measures['arms'], measures['forearms'], measures['hips'],
                    measures['height']])


def execute(measures):
    run_blender(blenderPath, projectPath, scriptPath, measures)


if __name__ == "__main__":
    # Example measures
    measures = {
        'head': '12',
        'torso': '30',
        'legs': '40',
        'calves': '20',
        'shoulders': '15',
        'arms': '10',
        'forearms': '8',
        'hips': '25',
        'height': '180'
    }
    execute(measures)
