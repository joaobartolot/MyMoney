var app = angular.module("RegistrationApp", []);

app.controller("RegistrationController", function($scope, $http) {
  $scope.username = "";
  $scope.password = "";
  $scope.password_confirmation = "";

  $scope.makeRequest = () => {
    username = $scope.username;
    password = $scope.password;
    password_confirmation = $scope.password_confirmation;

    $http({
      method: "POST",
      url: "/register/",
      xsrfHeaderName: "X-CSRFToken",
      xsrfCookieName: "csrftoken",

      data: {
        csrfmiddlewaretoken: csrfmiddlewaretoken,
        username: username,
        password1: password,
        password2: password_confirmation
      }
    });
  };
});
