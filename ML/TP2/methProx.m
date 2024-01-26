function prox_result = methProx(x, lambda_val)
    prox_result = sign(x) .* max(0, abs(x) - lambda_val);
end