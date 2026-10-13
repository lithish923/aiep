"""
EXPERIMENT 5 — INFERENCE SYSTEM
Source: 22IT702 LAB MANUAL (Pages 10–11)
"""

facts = ["rainy"]

rules = {
    "rainy": "carry_umbrella",
    "carry_umbrella": "stay_dry"
}

inferred = []

for fact in facts:
    if fact in rules:
        conclusion = rules[fact]
        inferred.append(conclusion)

        if conclusion in rules:
            inferred.append(rules[conclusion])

print("Facts:", facts)
print("Inferred Knowledge:", inferred)
