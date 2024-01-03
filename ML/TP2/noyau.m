
function noyau = noyau(x, x1, choix)
  switch choix
      case 1
          % Noyau linéaire
          c = 0.01; 
          y = x' * x1 + c;
      case 2
          % Noyau polynomial
          alpha = 0.05; % Valeur arbitraire pour alpha, vous pouvez ajuster selon vos besoins
          c = 0.01; % Valeur arbitraire pour c, vous pouvez ajuster selon vos besoins
          d = 1.2; % Valeur arbitraire pour d, vous pouvez ajuster selon vos besoins
          y = (alpha .* (x' * x1) + c) .^ d;
      case 3
          % Noyau gaussien
          sigma = 10; 
          y = exp( -norm(x - x1) .^ 2 ./ (2 * sigma ^ 2));
      case 4
          % Noyau exponentiel
          sigma = 5; 
          y = exp(-norm(x - x1) ./ (2 * sigma ^ 2));
      case 5
          % Noyau laplacien
          sigma = 1; 
          y = exp(-norm(x - x1) / sigma);
      case 6
          % Noyau sinc
          sigma = 5; 
          y = prod(sin(sigma * (x - x1)) ./ (sigma * (x - x1)));
      otherwise
          error('Type de noyau non reconnu.');
  end
  noyau = y;
end