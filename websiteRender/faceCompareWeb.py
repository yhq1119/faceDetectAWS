# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3, shutil
from flask import Flask, render_template
import io
from PIL import Image, ImageDraw, ExifTags, ImageColor

if __name__ == "__main__":

    sourceFile = 'static/pics/image01.jpg'
    targetFile = 'static/pics/image02.jpg'
    client = boto3.client('rekognition')

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    # imageResult = open(targetFile, 'wb')
    # # imgW, imgH = imageResult.size
    # draw = ImageDraw.Draw(imageResult)

    response = client.compare_faces(SimilarityThreshold=0, SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    shutil.copy('static/pics/image01.jpg', 'static/pics/src1.jpg')
    shutil.copy('static/pics/image02.jpg', 'static/pics/tar1.jpg')

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        result = 'The face at ' + str(position['Left']) + ' ' + str(
            position['Top']) + ' matches with ' + similarity + '% confidence'
    print(result)

app = Flask(__name__)


@app.route('/')
def hello_web():
    return render_template("faces.html", result1=result)


app.run(debug=True)

imageSource.close()
imageTarget.close()
