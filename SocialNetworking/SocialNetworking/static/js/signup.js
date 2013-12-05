'use strict';
angular.module('sign_up_app', [])
    .config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';    }
])
  .controller('SignupController', function($scope,$http) {
        $scope.submitForm = function() {
            $http.post('/create/',{"username":$scope.username,"password":$scope.password,"email": $scope.email})
                .success(function(data){
                    //success
                    alert(data)
                })
                .error(function(data){
                    //error
                })
        }

  })





//.directive('isUnique', function ($http) {
//         return function (scope, elm, attrs, ctrl) {
//
//            scope.watch("username",function(value) {
//                $http.post('/check_username/', {"username":value})
//                .success(function (data) {
//                     alert(data);
//                 })
//                 .error(function(data) {
//                     alert(data);
//                 })
//            })
//         }
//    });

//.directive("isUnqiue", function(){
//    return {
//        require:"ngModel",
//        link: function(scope, element, attr, ngModel){
//                scope.$watch(function(){
//                    return ngModel.$modelValue;
//                }, function(modelValue){
//                    //ajax
//                });
//            }
//    }
//});

