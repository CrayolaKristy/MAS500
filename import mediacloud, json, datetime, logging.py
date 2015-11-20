import mediacloud, json, datetime, logging

logging.basicConfig(filename="bees.log", filemode="w", level=logging.INFO)

my_api_key = 'a8031b00764a869d4af49778c040cdc38e170b76331a4a53c97afd0f5be3ae8b'
mc = mediacloud.api.MediaCloud(my_api_key)

logging.info('Connection Made!')

bees_2013 = mc.sentenceCount('(bee OR bees)', solr_filter=[mc.publish_date_query(datetime.date(2013,1,1), datetime.date(2014,1,1)), 'media_sets_id:1'])
logging.info('Count Bee or Bees from 2013')
bees_2014 = mc.sentenceCount('(bee OR bees)', solr_filter=[mc.publish_date_query(datetime.date(2014,1,1), datetime.date(2015,1,1)), 'media_sets_id:1'])
logging.info('Count Bee or Bees from 2014')

if (bees_2014['count'] > bees_2013['count']):
    print "Bees were mentioned more times in 2014 then in 2013!"
    print "%d times in 2014, %d times in 2013"% (bees_2014['count'],bees_2013['count'])
else :
    print "Bees were mentioned more times in 2013 then in 2014!"
    print "%d times in 2013, %d times in 2014"% (bees_2013['count'],bees_2014['count'])