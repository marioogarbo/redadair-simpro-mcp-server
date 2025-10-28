from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse
from typing import List, Dict, Optional
from datetime import date, datetime
from services.simpro import Simpro

# Initialize the MCP server
mcp = FastMCP(name="Redadair Simpro MCP", version="2.0", auth=None)

# Custom Endpoint: provide details about the mcp
@mcp.custom_route("/", methods=["GET"])
async def service_info(request: Request) -> JSONResponse:
    return JSONResponse(
        {"service": "Redadair Simpro MCP", "status": "running", "version": "v2.0"}
    )

# Initialize the Simpro service
simpro = Simpro()

@mcp.tool()
def get_companies() -> List[Dict]:
    """
    Use this tool to retrieve all companies from Redadair.
    """
    return simpro.get_companies()


@mcp.tool()
def get_employees(company_id: Optional[int] = None) -> List[Dict]:
    """
    Use this tool to retrieve all employees from a specific company or all companies.
    """
    return simpro.get_employees(company_id)


@mcp.tool()
def get_employee(company_id: int, employee_id: int):
    """
    Use this tool to retrieve details of a specific employee by ID from a specific company.
    """
    return simpro.get_employee(company_id, employee_id) 


@mcp.tool()
def get_customers(company_id: int):
    """
    Use this tool to retrieve a list of customers.
    """
    return simpro.get_customers(company_id=company_id)


@mcp.tool()
def get_customers_of_company(company_id: int) -> List[Dict]:
    """
    Use this tool to retrieve a list of customers of a specific company.
    """
    return simpro.get_customers_of_company(company_id=company_id)


@mcp.tool()
def get_jobs(company_id: int) -> List[Dict]:
    """
    Use this tool to retrieve a list of jobs of a specific company.
    """
    return simpro.get_jobs(company_id=company_id)


@mcp.tool()
def get_job(company_id: int, job_id: int) -> Dict:
    """
    Use this tool to retrieve details of a specific job by ID.
    """
    return simpro.get_job(company_id=company_id, job_id=job_id)


@mcp.tool()
def get_jobs_reports_ops(company_id: int, search: Optional[str] = None, date: Optional[str] = None) -> List[Dict]:
    """
    Use this tool to retrieve a list of jobs with operations of a specific company.
    """
    return simpro.get_jobs_reports_ops(company_id=company_id, search=search, date=date)


@mcp.tool()
def get_jobs_reports_financials(company_id: int) -> List[Dict]:
    """
    Use this tool to retrieve a list of jobs with financials of a specific company.
    """
    return simpro.get_jobs_reports_financials(company_id=company_id)


@mcp.tool()
def get_leads(company_id: int) -> List[Dict]:
    """
    Use this tool to retrieve a list of leads of a specific company.
    """
    return simpro.get_leads(company_id=company_id)


@mcp.tool()
def get_lead(company_id: int, lead_id: int) -> Dict:
    """
    Use this tool to retrieve details of a specific lead by ID.
    """
    return simpro.get_lead(company_id=company_id, lead_id=lead_id)


@mcp.tool()
def get_quotes(company_id: int) -> List[Dict]:
    """
    Use this tool to retrieve a list of quotes of a specific company.
    """
    return simpro.get_quotes(company_id=company_id)


@mcp.tool()
def get_quote(company_id: int, quote_id: int) -> Dict:
    """
    Use this tool to retrieve details of a specific quote by ID.
    """
    return simpro.get_quote(company_id=company_id, quote_id=quote_id)


def main():
    """Main entry point for the MCP server."""
    mcp.run(transport='streamable-http', host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()