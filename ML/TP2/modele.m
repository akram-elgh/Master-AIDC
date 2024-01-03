function fonction = modele(choice, x)
  switch choice
      case 1
          fonction = abs(x);
      case 2
          fonction = 3 .* norm(x) .^ 3 - 2 .* norm(x) .^ 2 + 3 .* norm(x) + 3;
      case 3
          fonction = sin(x + x);
      case 4
          fonction = abs((1/3 * (x + x) ^ 3 ) - (1/4 * (x + x)));
      otherwise
          disp('Invalid choice');
  end
end