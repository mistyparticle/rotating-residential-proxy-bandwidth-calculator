#!/usr/bin/env python3
"""
Rotating Residential Proxy Bandwidth & HTML Scraping Calculator 2026.
Estimates total payload and dollar cost per million target web pages scraped.
"""
import argparse

def estimate_scraping_bandwidth(page_count, avg_html_kb, rate_per_gb):
    total_kb = page_count * avg_html_kb
    total_gb = total_kb / (1024.0 * 1024.0)
    total_cost = total_gb * rate_per_gb
    cost_per_thousand = (total_cost / page_count) * 1000.0 if page_count > 0 else 0.0
    return {
        "total_gb": total_gb,
        "total_cost": total_cost,
        "cost_per_thousand": cost_per_thousand
    }

def main():
    parser = argparse.ArgumentParser(description="Scraping Bandwidth & Cost Estimator")
    parser.add_argument("--pages", type=float, default=250000.0, help="Number of pages scraped per month (default: 250,000)")
    parser.add_argument("--kb-per-page", type=float, default=120.0, help="Average payload per page in KB (default: 120)")
    parser.add_argument("--rate", type=float, default=3.50, help="Webshare residential rate per GB (default: $3.50)")
    args = parser.parse_args()

    res = estimate_scraping_bandwidth(args.pages, args.kb_per_page, args.rate)
    print(f"Total Pages Scraped:     {args.pages:,.0f} pages")
    print(f"Total Bandwidth:         {res['total_gb']:.2f} GB")
    print(f"Total Monthly Cost:      ${res['total_cost']:.2f}")
    print(f"Cost Per 1,000 Pages:    ${res['cost_per_thousand']:.4f}")

if __name__ == "__main__":
    main()
