# Tiered Phone Plan Calculator

The phone provider is introducing premium membership and new overage rates. Extend your completed [Phone Data Bill Calculator lab](https://github.com/cptc-computer-programming/cpw102-phone-bill-calculator) so customers can understand their bill under the new pricing policy.

Before beginning, follow [GITHUB_SETUP.md](GITHUB_SETUP.md).

## Learning Goals

- Extend an existing program while preserving behavior that still applies.
- Use `if-elif-else` and nested decisions to select a rate.
- Convert a text response into a Boolean value.
- Use function parameters and returned values in calculations and decisions.
- Combine conditions with logical operators.
- Test boundaries and compare results when one input changes.

## Adapt Your Lab

Keep your working lab. Replace its fixed overage rate with a function that selects the rate, then add premium membership.

> [!IMPORTANT]
> Open your completed lab's `03_execution/data_bill.py` beside this homework's `data_bill.py`. Copy the relevant code into the outline below; keep your lab repository unchanged.

| Function in the homework | What to put there |
| --- | --- |
| `exceeds_data_limit(data_used)` | Your lab's Boolean-returning data-limit check. Rename it if needed and update its calls. |
| `get_overage_rate(data_used, has_premium)` | New logic that returns the rate from the pricing table below. |
| `main()` | Your lab's existing inputs, calculations, usage decisions, and printed messages. Keep these together. |

1. Replace the `pass` in `exceeds_data_limit` with your existing check. Copy the rest of your program into `main()`; if your lab already has a `main()`, copy its body rather than defining it again.
2. Add the premium question in `main()` and convert the response into a Boolean variable.
3. Implement `get_overage_rate`. In `main()`, call it and use its returned rate instead of the fixed $2 rate.
4. Add the premium recommendation and test the updated program.


## New Pricing Policy

The plan still includes 10 GB. Ask whether the customer has premium membership in addition to their data usage and base plan cost.

| Total data used | Regular overage rate | Premium overage rate |
| --- | --- | --- |
| 10 GB or less | No overage charge | No overage charge |
| More than 10 GB, up to and including 20 GB | $2 per GB over the data limit | $1 per GB over the data limit |
| More than 20 GB | $3 per GB over the data limit | $2 per GB over the data limit |

> [!IMPORTANT]
> The selected rate applies to **all GB beyond the 10 GB data limit**, not just the portion in a particular tier. For example, a regular customer using 25 GB pays for 15 overage GB at $3 each.

> [!NOTE]
> Keep the lab's usage categories: up to 5 extra GB is moderate; more than 5 extra GB is high. These message categories are separate from the pricing tiers.

Recommend considering premium membership only when a regular customer exceeds the data limit. Do not add a membership fee or discount beyond the rates shown above.

## Implementation Requirements

Complete the three functions in `data_bill.py`:

- **Data-limit check:** Reuse your lab function and use its Boolean result in a decision in `main()`.
- **Overage rate:** Use `if-elif-else` for the usage tiers and a nested decision for premium pricing. Return the rate, or `0` within the data limit.
- **Main program:** Store premium status as a Boolean, ignoring capitalization and extra spaces in the response. Call the rate function, store the rate and overage GB, and use them to calculate the charges. Use logical operators for the premium recommendation.

Choose your own local variable names, prompts, and output layout.

## Assumptions

- Data usage and base cost will be numeric. 
- The membership response will be `yes` or `no`, possibly with different capitalization or surrounding spaces. 

## Output

Display the usage message, GB over the data limit, overage cost, and total monthly bill. Display the applicable rate when there is overage and the premium recommendation when its conditions are met. Show money amounts to two decimal places.

### Example: Within the Data Limit

```text
Enter data used (GB): 8
Enter base monthly plan cost: 40
Do you have premium membership? (yes or no): no

You are within your data limit.
GB over limit: 0.0
Overage cost: $0.00
Total bill: $40.00
```

### Example: Regular Customer with High Usage

```text
Enter data used (GB): 25
Enter base monthly plan cost: 40
Do you have premium membership? (yes or no): no

You are 15.0 GB over your limit.
High extra usage.
Overage rate: $3.00 per GB
Overage cost: $45.00
Total bill: $85.00
Consider premium membership to reduce your overage rate.
```

Your wording and spacing do not need to match the examples exactly.

## Testing

Run your program from the repository folder:

```text
python data_bill.py
```

Here are some example test cases you can use to confirm your program behaves as required.

| Data used (GB) | Base cost | Premium response | Focus |
| --- | --- | --- | --- |
| 20 | 40 | `no` | Upper boundary of the middle pricing tier |
| 20 | 40 | `yes` | Membership comparison at the same boundary |
| 20.5 | 40 | `no` | Just above the pricing boundary |
| 20.5 | 40 | `yes` | Premium rate above the boundary |



## Submission


See [GITHUB_SETUP.md](GITHUB_SETUP.md) for detailed instructions.
