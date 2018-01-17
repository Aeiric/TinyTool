import tinify
import os
import os.path

tinify.key = "A8XzAlrdQSHtMJrq-FHXUTpHfkg56CWA" # 你在tinypng官网申请的apikey
fromFilePath = "/Users/macbookair/Desktop/drawable-hdpi" # 你电脑上的待压缩图片文件夹目录(绝对路径)
toFilePath = "/Users/macbookair/Desktop/drawable-hdpi-t" # 你电脑上的待生成的图片文件夹目录(自定义名称，绝对路径)

for root, dirs, files in os.walk(fromFilePath):
	for name in files:
		fileName, fileSuffix = os.path.splitext(name)
		if fileSuffix == '.png' or fileSuffix == '.jpg':
			toFullPath = toFilePath + root[len(fromFilePath):]
			toFullName = toFullPath + '/' + name
			fromFullPath = fromFilePath + root[len(fromFilePath):]
			fromFullName = fromFullPath + '/' + name
			
			if os.path.isdir(toFullPath):
				pass
			else:
				os.mkdir(toFullPath)
			
			source = tinify.from_file(fromFullName)
			source.to_file(toFullName)
