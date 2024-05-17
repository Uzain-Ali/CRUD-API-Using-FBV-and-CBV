from rest_framework import serializers
from .models import Student

def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should starts with R')


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name','roll', 'city'] 
        # read_only_fields = ['name','roll']
        # extra_kwargs = {'name':{'read_only': True}

            # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
        
    #Object Level Validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')

        if name.lower() == 'hamza' and city.lower() != 'karachi':
                raise serializers.ValidationError('City must be Karachi')
        return data

