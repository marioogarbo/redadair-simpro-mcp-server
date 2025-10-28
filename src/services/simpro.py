import os
import requests
import json
from typing import Dict, Any, List, Optional
from datetime import date, datetime

from dotenv import load_dotenv
load_dotenv(override=True)

class Simpro():
    def __init__(self):
        self.base_url = os.getenv('SIMPRO_BASE_URL')
        self.access_token = os.getenv('SIMPRO_ACCESS_TOKEN')
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }


    def get_companies(self) -> List[Dict[str, Any]]:
        """
        Retrieve all companies from the API.
        """
        url = f"{self.base_url}/api/v1.0/companies/"
        try:
            response = requests.get(url, params={}, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching companies: {e}")
            return []


    def get_employees(self, company_id: Optional[int] = None) -> List[Dict]:
        """
        Retrieve all employees from a specific company or return a predefined list.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/employees/"
        try:
            response = requests.get(url, params={}, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching employees: {e}")
            return []


    def get_employee(self, company_id: int, employee_id: int) -> Dict:
        """
        Retrieve details of a specific employee by ID from a specific company.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/employees/{employee_id}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching employee {employee_id} for company {company_id}: {e}")
            return {}


    def get_customers(self, company_id: int) -> Dict:
        """
        Retrieve a list of customers.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/customers/"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching customers for company {company_id}: {e}")
            return {}


    def get_customer(self, company_id: int, customer_id: int) -> Dict:
        """
        Retrieve details of a specific customer by ID from a specific company.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/customers/companies/{customer_id}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching customer {customer_id} for company {company_id}: {e}")
            return {}


    def get_jobs(self, company_id: int) -> List[Dict]:
        """
        Retrieve all jobs from all companies.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/jobs/"

        try:
            response = requests.get(url, params={}, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching jobs for company {company_id}: {e}")
            return []


    def get_job(self, company_id: int, job_id: int) -> Dict:
        """
        Retrieve a specific job for a company.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/jobs/{job_id}/"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching job {job_id} for company {company_id}: {e}")
            return {}


    def get_job_attachments(self, company_id: int, job_id: int) -> List[Dict]:
        """
        Retrieve attachments for a specific job in a company.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/jobs/{job_id}/attachments/files/"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching attachments for job {job_id} in company {company_id}: {e}")
            return []


    def get_jobs_reports_ops(self, company_id: int, search: Optional[str] = None, date: Optional[str] = None) -> List[Dict]:
        """
        Retrieve job operation reports for a specific company.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/reports/jobs/costToComplete/operations/"
        parameters = {
            "search": search,
            "date": date
        }
        try:
            response = requests.get(url, params=parameters, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching jobs for company {company_id}: {e}")
            return []


    def get_jobs_reports_financials(self, company_id: int):
        """
        Retrieve job financial reports for a specific company.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/reports/jobs/costToComplete/financial/"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching jobs financials for company {company_id}: {e}")
            return []


    def get_customers_of_company(self, company_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve customers from a specific company.
        """   
        customer_endpoint = f"/api/v1.0/companies/{company_id}/customers/?limit=100"
        url = f"{self.base_url}{customer_endpoint}"
        
        try:
            response = requests.get(url, params={}, headers=self.headers)
            response.raise_for_status()
            customers = response.json()
        except Exception as e:
            print(f"Error fetching customers: {e}")
            return []
        
        customer_details = []
        
        for customer in customers:
            indx = customer['_href'].find('?')
            customer_endpoint = customer['_href'][:indx]
            url = f"{self.base_url}{customer_endpoint}"
    
            try:
                response = requests.get(url, params={}, headers=self.headers)
                response.raise_for_status()
                customer_data = response.json()
                customer_details.append(customer_data)
                
            except Exception as e:
                continue
        
        return customer_details


    def get_leads(self, company_id: int) -> List[Dict]:
        """
        Retrieve all leads from a specific company.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/leads/"
        try:
            response = requests.get(url, params={}, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching leads: {e}")
            return []


    def get_lead(self, company_id: int, lead_id: int) -> Dict:
        """
        Retrieve a specific lead for a company.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/leads/{lead_id}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching lead {lead_id} for company {company_id}: {e}")
            return {}


    def get_quotes(self, company_id: int, limit: Optional[int] = None) -> List[Dict]:
        """
        Retrieve all quotes from a specific company.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/quotes/"
        params = {
            "search": "all",
            "pageSize": "",
            "orderby": "",
            "limit": limit
        }
        try:
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching quotes: {e}")
            return []


    def get_quote(self, company_id: int, quote_id: int) -> Dict[str, Any]:
        """
        Retrieve a specific quote for a company.
        """
        url = f"{self.base_url}/api/v1.0/companies/{company_id}/quotes/{quote_id}/"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching quote {quote_id} for company {company_id}: {e}")
            return {}


if __name__ == "__main__":
    simpro = Simpro()

    # GET COMPANIES
    companies = simpro.get_companies()
    print(json.dumps(companies, indent=4))

    # GET EMPLOYEES
    # employees = simpro.get_employees(company_id=56)
    # print(json.dumps(employees, indent=4))

    # GET JOBS
    # jobs = simpro.get_jobs(company_id=56)
    # print(json.dumps(jobs, indent=4))

    # GET JOB ATTACHMENTS
    # job_attachments = simpro.get_job_attachments(company_id=56, job_id=12345)
    # print(json.dumps(job_attachments, indent=4))

    # GET EMPLOYEE DETAILS
    # employee_details = simpro.get_employee(company_id=56, employee_id=1718)
    # print(json.dumps(employee_details, indent=4))

    # GET JOBS FINANCIALS
    # jobs = simpro.get_jobs_financials(company_id=56)
    # print(json.dumps(jobs, indent=4))

    # GET LEADS
    # leads = simpro.get_leads(company_id=56)
    # print(json.dumps(leads, indent=4))

    # GET QUOTES
    # quotes = simpro.get_quotes(company_id=56)
    # print(json.dumps(quotes, indent=4))

    # GET CUSTOMERS
    # customers = simpro.get_customers(company_id=56)
    # print(json.dumps(customers, indent=4))

    # GET COMPANY CUSTOMERS
    # customers = simpro.get_customers(company_id=56)
    # print(json.dumps(customers, indent=4))

    # GET CUSTOMER DETAILS
    # customer_details = simpro.get_customer(company_id=56, customer_id=22935)
    # print(json.dumps(customer_details, indent=4))