BOT_NAME = 'johnsonfinancialgroup'

SPIDER_MODULES = ['johnsonfinancialgroup.spiders']
NEWSPIDER_MODULE = 'johnsonfinancialgroup.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'johnsonfinancialgroup.pipelines.JohnsonfinancialgroupPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
