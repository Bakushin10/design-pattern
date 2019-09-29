import abc


"""
example 1 
"""

class Interface(object, metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError("you need to implment this")

    @abc.abstractclassmethod
    def saveToLegacy(self, response):
        # convert reponse to model and save
        pass

class MyCar(Interface):
    def __init__(self):
        pass
    
    def __str__(self):
        return "this is my car"




"""
example 2 
"""

# Client
class Smartphone(object):

    max_input_voltage = 5

    @classmethod
    def outcome(cls, input_voltage):
        if input_voltage > cls.max_input_voltage:
            print("Input voltage: {}V -- BURNING!!!".format(input_voltage))
        else:
            print("Input voltage: {}V -- Charging...".format(input_voltage))

    def charge(self, input_voltage):
        """Charge the phone with the given input voltage."""
        self.outcome(input_voltage)

# Supplier
class Socket(object):
    output_voltage = None

class EUSocket(Socket):
    output_voltage = 230

class USSocket(Socket):
    output_voltage = 120

class CannotTransformVoltage(Exception):
    """Exception raised by the SmartphoneAdapter.

    This exception represents the fact that an adapter can not provide the
    right voltage to the Smartphone if the voltage of the Socket is wrong."""
    pass

class SmartPhoneAdaptor(Smartphone, Socket):

    @classmethod
    def transform_voltage(cls, input_voltage):
        if input_voltage == cls.output_voltage:
            return cls.max_input_voltage
        else:
            raise CannotTransformVoltage(
                "Can\'t transform {0}-{1}V. This adapter transforms {2}-{1}V."
                .format(input_voltage, cls.max_input_voltage, cls.output_voltage))
    
    @classmethod
    def charge(cls, input_voltage):
        try:
            voltage = cls.transform_voltage(input_voltage)
            cls.outcome(voltage)
        except CannotTransformVoltage as e:
            print(e)
        
class SmartphoneEUAdapter(SmartPhoneAdaptor, EUSocket):
    pass

class SmartphoneUSAdapter(SmartPhoneAdaptor, USSocket):
    """System (smartphone + adapter) for an American Socket."""
    pass


smarthone_with_eu_adapter = SmartphoneEUAdapter()
smarthone_with_eu_adapter.charge(EUSocket.output_voltage)