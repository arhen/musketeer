import os

def file_get_contents(path):
	if os.path.isfile(path):
		with open(path, 'r') as file:
			contents = file.read()

			return contents

def file_put_contents(path, contents):
	if os.path.isfile(path):
		os.remove(path)

	with open(path, 'w') as file:
		file.write(contents)

def make_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)

def install(destination):
	# Get all of the necessary files for building
	templates = {
		'config': file_get_contents('src/templates/config.php'),
		'database': file_get_contents('src/templates/database.php'),
		'index': file_get_contents('src/templates/index.php')
	}
	sources = {
		'security_check': file_get_contents('src/security_check.php'),
		'file_utils': file_get_contents('src/file_utils.php'),
		'installer': file_get_contents('src/installer.php'),
		'form': file_get_contents('src/form.php')
	}
	# Figure out where the final file should be built
	build_path = destination + '/install.php'

	# Compile the built file as a single, formatted string,
	# making sure to declare the templates array in global space
	build = '<?php' + '\n' + '$templates = array();' + '\n'

	for key, template in templates.items():
		build += '\n' + template.split('\n', 1)[1] + '\n'

	for key, source in sources.items():
		build += '\n' + source.split('\n', 1)[1] + '\n'

	# Create a folder for the build if it doesn't already exist
	make_dir(destination)

	# Write the built file to the build path
	file_put_contents(build_path, build)

	# Alert the user that the build completed
	print('Built installer at `', build_path, '`.')

if __name__ == '__main__':
	install('build')