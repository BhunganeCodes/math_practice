import numpy as np
import matplotlib.pyplot as plt

def breakeven_point(cost_A_params, cost_B_params):
    """
    Financial Analysis / Software Subscription Models context.

    Determine the usage unit 'u' where the total cost of Plan A equals
    the total cost of Plan B. Both costs follow a linear model: C(u) = F + M * u.

    Use matplotlib and numpy to help you visualize the two cost functions and their intersection point.

    Args:
        cost_A_params (list[float]): (F_A, M_A) - Fixed cost and marginal cost for Plan A.
        cost_B_params (list[float]): (F_B, M_B) - Fixed cost and marginal cost for Plan B.

    The breakeven point is found by solving F_A + M_A * u = F_B + M_B * u for u.

    Returns:
        float: The usage unit u at the breakeven point.
               Returns -1.0 if the marginal costs are equal (parallel lines).
    """

    fixed_A, marginal_A = cost_A_params
    fixed_B, marginal_B = cost_B_params

    if marginal_A == marginal_B:
        return -1

    return (fixed_A - fixed_B) / (marginal_B - marginal_A)

breakeven_point((50, 5), (100, 3))

def net_flow_accumulation(flow_rate_coefficients, time_start, time_end):
    """
    Water Resource Management / System Flow Rate context.

    Given a flow rate R(t) modeled by a quadratic function R(t) = a*t^2 + b*t + c,
    compute the total net accumulated amount over a time interval [time_start, time_end].

    This requires computing the definite integral of R(t) from time_start to time_end.

    Use matplotlib and numpy to help you visualize the flow rate function and the area under the curve.

    Args:
        flow_rate_coefficients (list[float]): (a, b, c) coefficients of the quadratic rate function.
        time_start (float): The starting time t_start.
        time_end (float): The ending time t_end.

    Returns:
        float: The total accumulated net amount (Volume) over the interval.
    """

    # The antiderivative F(t) is (a/3)*t^3 + (b/2)*t^2 + c*t
    # Result is F(time_end) - F(time_start)

    pass

net_flow_accumulation([50, -20, 5], 1, 3)