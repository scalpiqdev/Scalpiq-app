# Companion Planner Module
# Calculates smart trade plan with entry/exit, zones, and confidence scoring

def generate_trade_plan(premarket_gap, prev_close, high, low, support, resistance, trend):
    plan = {}
    
    # Determine directional bias
    if premarket_gap > 1.5:
        plan['bias'] = 'bullish'
    elif premarket_gap < -1.5:
        plan['bias'] = 'bearish'
    else:
        plan['bias'] = 'neutral'

    # Entry logic
    plan['entries'] = []
    if trend == 'bullish':
        plan['entries'].append({'type': 'breakout', 'level': resistance + 0.5})
        plan['entries'].append({'type': 'support bounce', 'level': support})
    elif trend == 'bearish':
        plan['entries'].append({'type': 'breakdown', 'level': support - 0.5})
        plan['entries'].append({'type': 'retest reject', 'level': resistance})
    else:
        plan['entries'].append({'type': 'range fade', 'level': (high + low) / 2})

    # Exit logic
    plan['exits'] = []
    for entry in plan['entries']:
        if plan['bias'] == 'bullish':
            plan['exits'].append({'target': entry['level'] + 2.0, 'stop': entry['level'] - 1.0})
        elif plan['bias'] == 'bearish':
            plan['exits'].append({'target': entry['level'] - 2.0, 'stop': entry['level'] + 1.0})
        else:
            plan['exits'].append({'target': entry['level'] + 1.0, 'stop': entry['level'] - 1.0})

    # No-trade zone logic
    plan['no_trade_zone'] = {
        'start': 11.5,
        'end': 13.0,
        'reason': 'Low volume lunch chop zone'
    }

    # Confidence scoring
    plan['confidence'] = 'A+' if abs(premarket_gap) >= 2 else 'B' if abs(premarket_gap) >= 1 else 'C'

    return plan