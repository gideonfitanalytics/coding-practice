import argparse
import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
import testReplaceModule

argv = None
parser = argparse.ArgumentParser()
parser.add_argument('--input',
                    dest='input',
                    default='testinput.tsv',
                    help='Input file to process.')
parser.add_argument('--output',
                    dest='output',
                    default='testoutput.tsv',
                    help='Output file to write results to.')
known_args, pipeline_args = parser.parse_known_args(argv)
pipeline_args.extend([
    '--runner=DirectRunner',
    '--project=SET_YOUR_PROJECT_ID_HERE',
    '--staging_location=gs://YOUR_BUCKET_NAME/AND_STAGING_DIRECTORY',
    '--temp_location=gs://YOUR_BUCKET_NAME/AND_TEMP_DIRECTORY',
    '--job_name=your-wordcount-job',
])

pipeline_options = PipelineOptions(pipeline_args)
pipeline_options.view_as(SetupOptions).save_main_session = True
p = beam.Pipeline(options=pipeline_options)
tsvInput = p | ReadFromText(known_args.input)
output = tsvInput | 'mapping' >> beam.Map(testReplaceModule.replaceTabs)
output | 'finalOutput' >> WriteToText(known_args.output)
p.run()
