var homeApp = angular.module("HomeApp", []);

homeApp.controller("HomeController", ($scope, $http) => {
  var self = $scope;

  self.owlCarouselConfig = {
    center: true,
    items: 2,
    loop: false,
    lazyLoad: true,
    margin: 10,
    onTranslated: function(slide) {
      self.list.forEach(function(account) {
        account.isSelected = false;
      });

      let index = slide.relatedTarget._current;
      let account = self.list[index];

      self.current = index;

      account.isSelected = true;

      self.$apply();
    }
    // responsive:{
    // 	0: {
    // 		center: true,
    // 		items:1
    // 	},
    // 	600: {
    // 		items:2
    // 	}
    // }
  };

  self.list = [];

  self.haveAccount = true;

  self.current = 0;

  $http({
    method: "GET",
    url: "api/account-user-list"
  }).then(response => {
    self.list = response.data;

    if (self.list.length == 0) self.haveAccount = false;

    self.list.forEach(function(account) {
      account.isSelected = false;
      account.balanceText = getCurrencyText(account.balance);
    });

    self.list[0].isSelected = true;
  });
});
