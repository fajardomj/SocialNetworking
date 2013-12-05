'use strict';
angular.module('profile_app', [])
    .config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
]).config(['$interpolateProvider',function($interpolateProvider){
        $interpolateProvider.startSymbol('//');
        $interpolateProvider.endSymbol('//');
    }])
  .controller('profileController', function($scope,$http) {
        $http.get('/get_users/')
            .success(function(data) {
                $scope.users = data;

            })
        $scope.home = function() {
            location.href='/home/'
        }


  })






