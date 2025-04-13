import subprocess

def run_inference(source_image_path, action):
    """Run the inference.py script with the given source image."""
    if action == 'static':
        command = [
            'python3', 'inference.py',
            '--driven_audio', '/home/ubuntu/SadTalker/examples/driven_audio/silence.wav',
            '--source_image', source_image_path,
            '--result_dir', f'/home/ubuntu/staticvideo',
            '--enhancer', 'gfpgan'
        ]
    elif action == 'response':
        command = [
            'python3', 'inference.py',
            '--driven_audio', '/home/ubuntu/SadTalker/examples/driven_audio/response.wav',
            '--source_image', source_image_path,
            '--result_dir', f'/home/ubuntu/genvideo',
            '--enhancer', 'gfpgan'
        ]

    # Check if the command was successful
    try:
        # Run the command and capture the output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the command was successful
        if result.returncode != 0:
            # Log the error message
            print(f"Command failed with return code {result.returncode}")
            print(f"Command output: {result.stdout}")
            print(f"Command error: {result.stderr}")
            raise RuntimeError(f"Error running inference.py: {result.stderr}")

        return result.stdout
    except Exception as e:
        # Log the exception
        print(f"Exception occurred in run_inference: {str(e)}")
        raise
