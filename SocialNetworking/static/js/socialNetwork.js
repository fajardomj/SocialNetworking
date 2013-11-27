/**
 * Created by Fajardo on 11/26/13.
 */
// / declare a module
var myapp = angular.module('socialNetwork', []);


function LoginController($scope) {

$scope.login = function() {
   $scope.username="Matt";
  };
}


