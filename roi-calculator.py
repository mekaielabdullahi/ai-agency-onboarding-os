"""
AI Agency ROI Calculator
Calculates return on investment for AI solutions based on baseline and current metrics.
"""

from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional, Dict
import json


@dataclass
class BaselineMetrics:
    """Baseline metrics captured before AI implementation"""

    # Cost Metrics
    monthly_labor_cost: float
    annual_labor_cost: float
    monthly_software_cost: float
    annual_software_cost: float
    monthly_overhead_cost: float = 0.0
    monthly_error_cost: float = 0.0

    # Time Metrics
    avg_task_completion_time: float  # minutes
    volume_per_period: int
    period_type: str  # 'day', 'week', 'month'
    rework_hours_per_week: float = 0.0

    # Quality Metrics
    error_rate_percentage: float
    accuracy_rate_percentage: float = 0.0
    quality_control_hours_per_week: float = 0.0
    cost_per_error: float = 0.0

    # Customer Satisfaction Metrics
    nps_score: Optional[int] = None
    csat_score: Optional[float] = None
    complaints_per_month: int = 0
    avg_response_time_hours: float = 0.0
    churn_rate_percentage: float = 0.0

    # Sales/Revenue Metrics
    conversion_rate_percentage: float = 0.0
    avg_deal_size: float = 0.0
    sales_cycle_days: int = 0
    lead_response_time_hours: float = 0.0
    leads_per_month: int = 0
    monthly_revenue: float = 0.0
    estimated_monthly_lost_revenue: float = 0.0

    @property
    def total_monthly_cost(self) -> float:
        """Calculate total monthly operational cost"""
        return (
            self.monthly_labor_cost +
            self.monthly_software_cost +
            self.monthly_overhead_cost +
            self.monthly_error_cost
        )

    @property
    def total_annual_cost(self) -> float:
        """Calculate total annual operational cost"""
        return self.total_monthly_cost * 12


@dataclass
class CurrentMetrics:
    """Current metrics after AI implementation"""

    # Same fields as BaselineMetrics
    monthly_labor_cost: float
    annual_labor_cost: float
    monthly_software_cost: float
    annual_software_cost: float
    monthly_overhead_cost: float = 0.0
    monthly_error_cost: float = 0.0

    avg_task_completion_time: float
    volume_per_period: int
    period_type: str
    rework_hours_per_week: float = 0.0

    error_rate_percentage: float
    accuracy_rate_percentage: float = 0.0
    quality_control_hours_per_week: float = 0.0
    cost_per_error: float = 0.0

    nps_score: Optional[int] = None
    csat_score: Optional[float] = None
    complaints_per_month: int = 0
    avg_response_time_hours: float = 0.0
    churn_rate_percentage: float = 0.0

    conversion_rate_percentage: float = 0.0
    avg_deal_size: float = 0.0
    sales_cycle_days: int = 0
    lead_response_time_hours: float = 0.0
    leads_per_month: int = 0
    monthly_revenue: float = 0.0
    estimated_monthly_lost_revenue: float = 0.0

    # Additional tracking
    ai_solution_monthly_cost: float = 0.0
    system_uptime_percentage: float = 100.0
    user_adoption_rate: float = 100.0

    @property
    def total_monthly_cost(self) -> float:
        """Calculate total monthly operational cost including AI solution"""
        return (
            self.monthly_labor_cost +
            self.monthly_software_cost +
            self.monthly_overhead_cost +
            self.monthly_error_cost +
            self.ai_solution_monthly_cost
        )

    @property
    def total_annual_cost(self) -> float:
        """Calculate total annual operational cost"""
        return self.total_monthly_cost * 12


@dataclass
class ROICalculation:
    """ROI calculation results"""

    client_name: str
    project_name: str
    calculation_date: date
    period_analyzed: str  # e.g., "3 months", "6 months"

    # Investment
    total_implementation_cost: float
    monthly_ai_solution_cost: float

    # Cost Savings
    monthly_labor_cost_savings: float
    monthly_software_cost_savings: float
    monthly_overhead_savings: float
    monthly_error_cost_savings: float
    total_monthly_savings: float
    total_annual_savings: float

    # Efficiency Gains
    time_savings_percentage: float
    time_savings_hours_per_week: float
    error_reduction_percentage: float
    quality_improvement_percentage: float

    # Revenue Impact
    revenue_increase_monthly: float
    revenue_increase_annual: float
    conversion_rate_improvement: float
    customer_satisfaction_improvement: float

    # ROI Metrics
    net_monthly_benefit: float
    net_annual_benefit: float
    roi_percentage: float
    payback_period_months: float

    # Cumulative (based on period analyzed)
    cumulative_costs: float
    cumulative_savings: float
    cumulative_net_benefit: float

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'client_name': self.client_name,
            'project_name': self.project_name,
            'calculation_date': self.calculation_date.isoformat(),
            'period_analyzed': self.period_analyzed,
            'investment': {
                'total_implementation_cost': round(self.total_implementation_cost, 2),
                'monthly_ai_solution_cost': round(self.monthly_ai_solution_cost, 2)
            },
            'cost_savings': {
                'monthly_labor_cost_savings': round(self.monthly_labor_cost_savings, 2),
                'monthly_software_cost_savings': round(self.monthly_software_cost_savings, 2),
                'monthly_overhead_savings': round(self.monthly_overhead_savings, 2),
                'monthly_error_cost_savings': round(self.monthly_error_cost_savings, 2),
                'total_monthly_savings': round(self.total_monthly_savings, 2),
                'total_annual_savings': round(self.total_annual_savings, 2)
            },
            'efficiency_gains': {
                'time_savings_percentage': round(self.time_savings_percentage, 2),
                'time_savings_hours_per_week': round(self.time_savings_hours_per_week, 2),
                'error_reduction_percentage': round(self.error_reduction_percentage, 2),
                'quality_improvement_percentage': round(self.quality_improvement_percentage, 2)
            },
            'revenue_impact': {
                'revenue_increase_monthly': round(self.revenue_increase_monthly, 2),
                'revenue_increase_annual': round(self.revenue_increase_annual, 2),
                'conversion_rate_improvement': round(self.conversion_rate_improvement, 2),
                'customer_satisfaction_improvement': round(self.customer_satisfaction_improvement, 2)
            },
            'roi_metrics': {
                'net_monthly_benefit': round(self.net_monthly_benefit, 2),
                'net_annual_benefit': round(self.net_annual_benefit, 2),
                'roi_percentage': round(self.roi_percentage, 2),
                'payback_period_months': round(self.payback_period_months, 2)
            },
            'cumulative': {
                'cumulative_costs': round(self.cumulative_costs, 2),
                'cumulative_savings': round(self.cumulative_savings, 2),
                'cumulative_net_benefit': round(self.cumulative_net_benefit, 2)
            }
        }

    def generate_summary(self) -> str:
        """Generate a human-readable summary"""
        summary = f"""
ROI CALCULATION SUMMARY
=======================
Client: {self.client_name}
Project: {self.project_name}
Period Analyzed: {self.period_analyzed}
Calculation Date: {self.calculation_date.strftime('%Y-%m-%d')}

INVESTMENT
----------
Implementation Cost: ${self.total_implementation_cost:,.2f}
Monthly AI Solution Cost: ${self.monthly_ai_solution_cost:,.2f}

COST SAVINGS
------------
Monthly Labor Savings: ${self.monthly_labor_cost_savings:,.2f}
Monthly Software Savings: ${self.monthly_software_cost_savings:,.2f}
Monthly Error Cost Savings: ${self.monthly_error_cost_savings:,.2f}
Total Monthly Savings: ${self.total_monthly_savings:,.2f}
Total Annual Savings: ${self.total_annual_savings:,.2f}

EFFICIENCY GAINS
----------------
Time Savings: {self.time_savings_percentage:.1f}% ({self.time_savings_hours_per_week:.1f} hours/week)
Error Reduction: {self.error_reduction_percentage:.1f}%
Quality Improvement: {self.quality_improvement_percentage:.1f}%

REVENUE IMPACT
--------------
Monthly Revenue Increase: ${self.revenue_increase_monthly:,.2f}
Annual Revenue Increase: ${self.revenue_increase_annual:,.2f}
Conversion Rate Improvement: {self.conversion_rate_improvement:.2f} percentage points
Customer Satisfaction Improvement: {self.customer_satisfaction_improvement:.1f} points

ROI METRICS
-----------
Net Monthly Benefit: ${self.net_monthly_benefit:,.2f}
Net Annual Benefit: ${self.net_annual_benefit:,.2f}
ROI: {self.roi_percentage:.1f}%
Payback Period: {self.payback_period_months:.1f} months

CUMULATIVE ({self.period_analyzed})
-----------
Total Investment: ${self.cumulative_costs:,.2f}
Total Savings/Gains: ${self.cumulative_savings:,.2f}
Net Benefit: ${self.cumulative_net_benefit:,.2f}
        """
        return summary.strip()


class ROICalculator:
    """Calculate ROI based on baseline and current metrics"""

    def __init__(
        self,
        client_name: str,
        project_name: str,
        baseline: BaselineMetrics,
        current: CurrentMetrics,
        implementation_cost: float,
        months_since_deployment: int
    ):
        self.client_name = client_name
        self.project_name = project_name
        self.baseline = baseline
        self.current = current
        self.implementation_cost = implementation_cost
        self.months_since_deployment = months_since_deployment

    def calculate(self) -> ROICalculation:
        """Perform comprehensive ROI calculation"""

        # Cost Savings
        monthly_labor_savings = self.baseline.monthly_labor_cost - self.current.monthly_labor_cost
        monthly_software_savings = self.baseline.monthly_software_cost - self.current.monthly_software_cost
        monthly_overhead_savings = self.baseline.monthly_overhead_cost - self.current.monthly_overhead_cost
        monthly_error_savings = self.baseline.monthly_error_cost - self.current.monthly_error_cost

        total_monthly_savings = (
            monthly_labor_savings +
            monthly_software_savings +
            monthly_overhead_savings +
            monthly_error_savings
        )
        total_annual_savings = total_monthly_savings * 12

        # Efficiency Gains
        if self.baseline.avg_task_completion_time > 0:
            time_savings_pct = (
                (self.baseline.avg_task_completion_time - self.current.avg_task_completion_time) /
                self.baseline.avg_task_completion_time * 100
            )
        else:
            time_savings_pct = 0.0

        time_savings_hours_per_week = (
            self.baseline.rework_hours_per_week +
            self.baseline.quality_control_hours_per_week -
            self.current.rework_hours_per_week -
            self.current.quality_control_hours_per_week
        )

        error_reduction_pct = self.baseline.error_rate_percentage - self.current.error_rate_percentage
        quality_improvement_pct = self.current.accuracy_rate_percentage - self.baseline.accuracy_rate_percentage

        # Revenue Impact
        revenue_increase_monthly = self.current.monthly_revenue - self.baseline.monthly_revenue

        # Additional revenue from improved conversion
        if self.baseline.conversion_rate_percentage > 0:
            conversion_improvement = (
                self.current.conversion_rate_percentage - self.baseline.conversion_rate_percentage
            )
            # Estimate additional revenue from conversion improvement
            if self.current.leads_per_month > 0 and self.current.avg_deal_size > 0:
                additional_conversions = (
                    self.current.leads_per_month * (conversion_improvement / 100)
                )
                revenue_from_conversion = additional_conversions * self.current.avg_deal_size
                revenue_increase_monthly += revenue_from_conversion
        else:
            conversion_improvement = 0.0

        revenue_increase_annual = revenue_increase_monthly * 12

        # Customer Satisfaction
        if self.baseline.nps_score is not None and self.current.nps_score is not None:
            nps_improvement = self.current.nps_score - self.baseline.nps_score
        else:
            nps_improvement = 0.0

        if self.baseline.csat_score is not None and self.current.csat_score is not None:
            csat_improvement = self.current.csat_score - self.baseline.csat_score
        else:
            csat_improvement = 0.0

        # Use whichever satisfaction metric is available
        satisfaction_improvement = max(nps_improvement, csat_improvement)

        # ROI Calculation
        net_monthly_benefit = total_monthly_savings + revenue_increase_monthly - self.current.ai_solution_monthly_cost
        net_annual_benefit = net_monthly_benefit * 12

        # Cumulative calculation
        cumulative_costs = self.implementation_cost + (self.current.ai_solution_monthly_cost * self.months_since_deployment)
        cumulative_savings = (total_monthly_savings * self.months_since_deployment) + (revenue_increase_monthly * self.months_since_deployment)
        cumulative_net_benefit = cumulative_savings - cumulative_costs

        # ROI percentage: (Net Benefit / Total Investment) * 100
        if cumulative_costs > 0:
            roi_percentage = (cumulative_net_benefit / cumulative_costs) * 100
        else:
            roi_percentage = 0.0

        # Payback period: Total Investment / Monthly Net Benefit
        if net_monthly_benefit > 0:
            payback_period_months = self.implementation_cost / net_monthly_benefit
        else:
            payback_period_months = float('inf')

        # Determine period analyzed
        if self.months_since_deployment < 3:
            period_analyzed = f"{self.months_since_deployment} months"
        elif self.months_since_deployment < 12:
            period_analyzed = f"{self.months_since_deployment} months"
        else:
            years = self.months_since_deployment // 12
            remaining_months = self.months_since_deployment % 12
            if remaining_months == 0:
                period_analyzed = f"{years} year{'s' if years > 1 else ''}"
            else:
                period_analyzed = f"{years} year{'s' if years > 1 else ''} {remaining_months} months"

        return ROICalculation(
            client_name=self.client_name,
            project_name=self.project_name,
            calculation_date=date.today(),
            period_analyzed=period_analyzed,
            total_implementation_cost=self.implementation_cost,
            monthly_ai_solution_cost=self.current.ai_solution_monthly_cost,
            monthly_labor_cost_savings=monthly_labor_savings,
            monthly_software_cost_savings=monthly_software_savings,
            monthly_overhead_savings=monthly_overhead_savings,
            monthly_error_cost_savings=monthly_error_savings,
            total_monthly_savings=total_monthly_savings,
            total_annual_savings=total_annual_savings,
            time_savings_percentage=time_savings_pct,
            time_savings_hours_per_week=time_savings_hours_per_week,
            error_reduction_percentage=error_reduction_pct,
            quality_improvement_percentage=quality_improvement_pct,
            revenue_increase_monthly=revenue_increase_monthly,
            revenue_increase_annual=revenue_increase_annual,
            conversion_rate_improvement=conversion_improvement,
            customer_satisfaction_improvement=satisfaction_improvement,
            net_monthly_benefit=net_monthly_benefit,
            net_annual_benefit=net_annual_benefit,
            roi_percentage=roi_percentage,
            payback_period_months=payback_period_months,
            cumulative_costs=cumulative_costs,
            cumulative_savings=cumulative_savings,
            cumulative_net_benefit=cumulative_net_benefit
        )


# Example Usage
if __name__ == "__main__":
    # Example: E-commerce customer service automation
    baseline = BaselineMetrics(
        monthly_labor_cost=18000,  # 3 FTE @ $6k/month
        annual_labor_cost=216000,
        monthly_software_cost=500,
        annual_software_cost=6000,
        monthly_overhead_cost=2000,
        monthly_error_cost=1500,
        avg_task_completion_time=25,  # minutes per ticket
        volume_per_period=2000,  # tickets per month
        period_type='month',
        rework_hours_per_week=15,
        error_rate_percentage=12.0,
        accuracy_rate_percentage=88.0,
        quality_control_hours_per_week=20,
        cost_per_error=25,
        nps_score=35,
        csat_score=72.0,
        complaints_per_month=45,
        avg_response_time_hours=4.5,
        churn_rate_percentage=8.0,
        conversion_rate_percentage=0.0,  # Not applicable for this use case
        monthly_revenue=0.0,  # Indirect revenue impact
    )

    current = CurrentMetrics(
        monthly_labor_cost=9000,  # Reduced to 1.5 FTE
        annual_labor_cost=108000,
        monthly_software_cost=500,
        annual_software_cost=6000,
        monthly_overhead_cost=1000,
        monthly_error_cost=400,
        avg_task_completion_time=8,  # AI handles first response quickly
        volume_per_period=2800,  # Can handle more with same staff
        period_type='month',
        rework_hours_per_week=4,
        error_rate_percentage=3.5,
        accuracy_rate_percentage=96.5,
        quality_control_hours_per_week=8,
        cost_per_error=25,
        nps_score=58,
        csat_score=89.0,
        complaints_per_month=12,
        avg_response_time_hours=0.5,  # AI instant response
        churn_rate_percentage=4.5,
        ai_solution_monthly_cost=2500,  # AI platform + maintenance
        system_uptime_percentage=99.5,
        user_adoption_rate=95.0,
        monthly_revenue=0.0,
    )

    calculator = ROICalculator(
        client_name="Acme E-commerce Inc.",
        project_name="AI Customer Service Automation",
        baseline=baseline,
        current=current,
        implementation_cost=25000,  # Initial setup, training, integration
        months_since_deployment=6
    )

    roi = calculator.calculate()

    # Print summary
    print(roi.generate_summary())
    print("\n" + "="*50 + "\n")

    # Export to JSON
    with open('roi-calculation-example.json', 'w') as f:
        json.dump(roi.to_dict(), f, indent=2)

    print("ROI calculation exported to: roi-calculation-example.json")
