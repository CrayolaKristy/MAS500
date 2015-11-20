

import mediacloud, datetime
file_api = open('mc-key.txt', 'r')
api_key = file_api.read()

mc = mediacloud.api.MediaCloud(api_key)


res_trump = mc.sentenceCount('( trump )', solr_filter=[mc.publish_date_query( datetime.date( 2015, 8, 1), datetime.date( 2015, 9, 1) ), 'media_sets_id:1' ])
print res_trump['count'] # prints the number of sentences found

res_obama = mc.sentenceCount('( obama )', solr_filter=[mc.publish_date_query( datetime.date( 2015, 8, 1), datetime.date( 2015, 9, 1) ), 'media_sets_id:1' ])
print res_obama['count'] # prints the number of sentences found

if res_trump['count'] > res_obama['count']:
    print 'Trump more!'
elif res_trump['count'] < res_obama['count']:
    print 'Obama more!'
else:
    print 'Trump Obama equal!'