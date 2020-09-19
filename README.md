# django-task-4
## Task 1. Prepare Product table
## Prepare a table that contains Products using model and model fields. Let the products have the following attributes:
  - id (number type)
  - name (character type)
  - description (text type)
  - category (character type)
  - picture (image file type)
  - amount (number type)
  - price (decimal digits type)
  - production date (date and time type)
  - is new (binary type)
  - certificate (file type)
  - rating (decimal digits type)
  - detailed view link (web address (url) type)
-------------------------------------------------------------------------------------------------------
## Task 2.Product Model options
## Product model attributes give you create the following features:
  - name - can have a maximum of 125 characters. name must be unique.
  - description - can have a maximum of 500 characters.
  - category - can have a maximum of 125 characters. Must have different choices. Choices can
  be: Convenience Goods, Shopping Goods, Specialty Goods, etc.
  - picture - upload the image to the 'project_name / media / products / images /' folder
  - amount - equal to 0 by default.
  - The price is 0.00 per default. The number can be 5 digits before the comma and 2 after the
  comma.
  - production date (date and time type) - equal to the default creation date.
  - is new (binary type) - set to false by default.
  - certificate (file type) - Upload the file to the 'project_name / media / products / files /' folder.
  Not required to be added.
  - rating (decimal digits type) - 0.0 by default. The number can be 1 before the comma and 1
  after the comma. Not required to be added.
  - detailed view link (web address (url) type) - can have a maximum of 300 characters. Not
  required to be added. Let this attribute get a null value.
--------------------------------------------------------------------------------------------------------
## Task 3. Set Product Meta options and create table
## Change the meta options to the product model as follows:
  - verbose name must be "Product".
  - verbose plural name must be "Products".
  - table name must be "company_products".
  - Products must be ordered by “name” attribute.
