# Tutorial project for Django - AWS CI-CD CodePipeline workflow

GitHub branch -> AWS CodePipeline -> AWS CodeDeploy -> AWS Elastic Compute Cloud

## Original How-To Guide
[AWS CI-CD for your Django app with AWS CodePipeline](https://medium.com/clairvoyantblog/aws-ci-cd-for-your-django-app-with-aws-codepipeline-aafec23f9e55)

## HMP Data Integration with SRA Data Files:
- app/hmp_data_ingestion_v1.py - initial screen scraping of HMP frontend tables with minimal metadata collected
- app/hmp_data_ingestion_v2.py - secondary screen scraping of HMP frontend tables with extended metadata collected
- app/hmp_data_ingestion_v3.py - enhanced functionality to connect SRA IDs to HMP IDs with download file links and salted UUID created

## Next Steps:
- Data Discovery Work - Understand where to find the SRA ACC ID, and also how to distinguish the connection between SRA (one ID) to HMP (many IDs) relationship. There are a lot of HMP IDs and files related to a single SRA ID. Which IDs are important to keep v. remove? Which files should be kepy v. removed?
- Data Quality Work - There is a lot of data quality issues which require being accessed and fixed in comparing SRA metadata and HMP metadata. This is imperative for resolution as it will greatly improve frontend search capabilities.
- Data Integration Work - The HMP data functionality needs to be integrated into the SRA API once data discovery and data quality work are completed. Then functional testing can be done to access if the results pushing to the S3 bucket are in fact as intended in results for the data engineering pipeline.
