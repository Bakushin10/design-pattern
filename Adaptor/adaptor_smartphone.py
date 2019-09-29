# Client
class Smartphone(object):

    max_input_voltage = 400

    @classmethod
    def outcome(cls, input_voltage):
        print("{} {} {}".format(input_voltage, cls.max_input_voltage, cls))
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


class EUAdapter(object):
    """EUAdapter encapsulates client (Smartphone) and supplier (EUSocket)."""
    input_voltage = EUSocket.output_voltage
    #if Smartphone.max_input_voltage < input_voltage
    output_voltage = Smartphone.max_input_voltage if Smartphone.max_input_voltage < input_voltage else input_voltage 
    #output_voltage = Smartphone.max_input_voltage

smartphone = Smartphone()
smartphone.charge(EUAdapter.output_voltage)


    

