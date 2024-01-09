function fonction = modele(choice, x)
  switch choice
      case 1
          fonction = abs(x);
      case 2
        %   x1 = x(:, 1);
        %   x2 = x(:, 2);
        %   x3 = x(:, 3);
        %   for i = 1:length(x1)
            fonction = 3 * norm(x) ^ 3 - 2 * norm(x) ^ 2 + 3 .* norm(x) + 3;
        %   end  
      case 3
          x1 = x(:, 1);
          x2 = x(:, 2); 
          fonction = sin(x1 + x2);
      case 4
          x1 = x(:, 1);
          x2 = x(:, 2); 
          fonction = abs((1/3 * (x1 + x2) .^ 3 ) - (1/4 * (x1 + x2)));
      otherwise
          disp('Invalid choice');
  end
end