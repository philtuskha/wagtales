from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.safestring import mark_safe

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock




# Content Blocks below
#---------------------------------------	

class PersonBlock(blocks.StructBlock):
	"""
	PersonBlock is an example of a sub-block / component / pre-defined collection of HTML elements.  
	This block could be used within the body of any page or within other blocks of other types.
	The idea is to be able to replicate this form of content
	"""
	first_name = blocks.CharBlock(required=True, classname="fname")
	surname = blocks.CharBlock(required=True)
	photo = ImageChooserBlock()
	biography = blocks.RichTextBlock()

	class Meta:
		template = 'home/blocks/person.html'
		icon = 'user'


class DrinksChoiceBlock(blocks.ChoiceBlock):
	"""
	simple dropdown on the admin side.
	"""
	choices = [
		('tea', 'Tea'),
		('coffee', 'Coffee'),
	]
	class Meta:
		icon = 'user'

# class ContentChoiceBlock(blocks.ChoiceBlock):
# 	"""
# 	FAKE EXAMPLE!!!! This would be useful if this somehow exsists for our purposes.
# 	you would use inside structural blocks ('choose', ContentChoiceBlock()),  
# 	"""
# 	choices = [
# 		('image', ImageChooserBlock()),
#         ('person', PersonBlock()),
#         ('drink', DrinksChoiceBlock()),
# 	]
# 	class Meta:
# 		icon = 'user'


class Thirds(blocks.StructBlock):
	"""1/3 width of the screen.  The idea here is that content type is flexable and based around structure.  
	Any content block that is split into thirds can be made to work inside here based on using StreamBlocks.
	Limitations are that there are no limitation.  Stream blocks allow you to keep adding content to them.  
	An either/or block solution would be ideal for this structure based approach.    

	"""
	thirds_heading = blocks.CharBlock(classname="full title")

	one_of_three = blocks.StreamBlock([
        ('image', ImageChooserBlock()),
        ('person', PersonBlock()),
        ('drink', DrinksChoiceBlock())])

	two_of_three = blocks.StreamBlock([
    	('image', ImageChooserBlock()),
    	('person', PersonBlock())])

	three_of_three = blocks.StreamBlock([
        ('image', ImageChooserBlock()),
        ('person', PersonBlock())])

	class Meta:
		icon = 'placeholder'
		template = 'home/blocks/thirds.html'
		

class Halves(blocks.StructBlock):
	"""
	HalvesBlock is an example of a sub-block / component / pre-defined collection of HTML elements.  
	Using StructBlock sets this overall block to have a specific predefined format.
	This block can only consist of photo - title - text, and these fields are required.

	"""
	one_of_two = blocks.StructBlock([
		('photo', ImageChooserBlock(classname="img")),
		('title', blocks.CharBlock(required=True, classname="title")),
		('text', blocks.RichTextBlock())])

	two_of_two = blocks.StructBlock([
		('photo', ImageChooserBlock(classname="img")),
		('title', blocks.CharBlock(required=True, classname="title")),
		('text', blocks.RichTextBlock())])


	class Meta:
		template = 'home/blocks/halves.html'
		icon = 'placeholder'

class SidebarBlock(blocks.StructBlock):
	"""
	HalvesBlock is an example of a sub-block / component / pre-defined collection of HTML elements.  
	Using StructBlock sets this overall block to have a specific predefined format.
	This block can only consist of photo - title - text, and these fields are required.

	"""
	main_content = blocks.StreamBlock([
		('heading', blocks.CharBlock()),
        ('image', ImageChooserBlock()),
        ('text', blocks.TextBlock()),
        ('person', PersonBlock()),
        ('drink', DrinksChoiceBlock())])

	sidebar = blocks.StreamBlock([
		('heading', blocks.CharBlock()),
        ('image', ImageChooserBlock()),
        ('text', blocks.TextBlock()),
        ('person', PersonBlock()),
        ('drink', DrinksChoiceBlock())])


	class Meta:
		template = 'home/blocks/sidebar.html'
		icon = 'placeholder'
		form_classname = 'side-bar'


class ListItemBlock(blocks.StructBlock):
	"""
	ListItemBlock is an example of a never ending list.  keep adding entries!  
	All content is manually entered. 
	"""
	list_title = blocks.CharBlock(classname="bloat_fork")
	list_item = blocks.ListBlock(blocks.StructBlock([
		    ('ingredient', blocks.CharBlock(required=True)),
		    ('amount', blocks.CharBlock()),    
		]))

	class Meta:
		icon = 'placeholder'
		template = 'home/blocks/list.html'


class ChildList(blocks.StructBlock):
	"""
	building automatic list based on child pages.  Using a StaticBlock allows admin-facing block.    
	Any content generating happens in this blocks template.  Currently referencing a function to find child page urls and linking to them.
	Might need to use app-tags to get further content from page (e.g. featured image or snippet/blurb)? 
	"""
	child_page_list = blocks.StaticBlock(admin_text=mark_safe('This block will grab child pages of this page and output clickable list'))

	class Meta:
		template = 'home/blocks/child_list.html'
		icon = 'placeholder'
		# label = 'use label to bypass "childs" (not sure when this is useful)'


# Page models below
#-----------------------------------------------

class WYSIWYGPage(Page):
	"""
	This page is fully edited by client via wysiwyg editor.  Desigers/Developers have very little control. 
	Guessing we want to steer away from this page model?
	"""
	body = RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('body', classname="full"),
	]

class InternalPage(Page):
	"""
	This is a catch all page with a multitude of block choices for content.  
	"""
	body = StreamField([
		('heading', blocks.CharBlock(classname="full title")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('halves', Halves()),
		('thirds', Thirds()),
		('person', PersonBlock()),
		('list', ListItemBlock()),
		('block_with_sidebar', SidebarBlock(classname = "main_dubs")),
		('drink', DrinksChoiceBlock()),
		('childs', ChildList()),
		('choose_page', blocks.PageChooserBlock()),
		('ingredients_list', blocks.ListBlock(blocks.StreamBlock([
		    ('ingredient', blocks.CharBlock(required=True)),
		    ('amount', blocks.CharBlock()),	    
		]))),
		('carousel', blocks.StreamBlock( 
		    [
		        ('image', ImageChooserBlock()),
		        ('quotation', blocks.StructBlock([
		            ('text', blocks.TextBlock()),
		            ('author', blocks.CharBlock()),
		        ])),
		        ('halves', Halves(classname="full title")),
		        ('person', PersonBlock()),

		        # ('video', EmbedBlock()),
		    ],
		    icon='cogs'
		))
	])

	content_panels = Page.content_panels + [
		StreamFieldPanel('body')
	]

class TemplatePage(Page):
	"""
	More of a traditional template page type with only one section with stream fileds.  
	the top and bottom rtf blocks are required    
	"""
	top = RichTextField(blank=True)

	middle = StreamField([
		('heading', blocks.CharBlock(classname="full title")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('halves', Halves(classname="full title")),
		('person', PersonBlock()),
		('list', ListItemBlock()),
		('thirds', Thirds())
	])

	bottom = RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('top'),
		StreamFieldPanel('middle'),
		FieldPanel('bottom'),
	]




