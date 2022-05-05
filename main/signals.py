from .models import Book, Comics, Author, Publisher
from django.dispatch import receiver
from django.db.models.signals import post_save
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Book)
def book_created(sender, instance, created, **kwargs):
    if created:
        logger.debug('created')
        logger.info('created')
        logger.warning('created')
        logger.error('created')
        logger.critical('created')

@receiver(post_save, sender=Comics)
def comics_created(sender, instance, created, **kwargs):
    if created:
        logger.debug('created')
        logger.info('created')
        logger.warning('created')
        logger.error('created')
        logger.critical('created')

@receiver(post_save, sender=Author)
def author_created(sender, instance, created, **kwargs):
    if created:
        logger.debug('created')
        logger.info('created')
        logger.warning('created')
        logger.error('created')
        logger.critical('created')

@receiver(post_save, sender=Publisher)
def publisher_created(sender, instance, created, **kwargs):
    if created:
        logger.debug('created')
        logger.info('created')
        logger.warning('created')
        logger.error('created')
        logger.critical('created')