class LeakyBucket:
    def __init__(self, bucket_size, output_rate, packets):
        self.bucket_size = bucket_size
        self.output_rate = output_rate
        self.packets = packets

    def traffic_shaping(self):
        for i in range(len(self.packets)):
            packet_size = self.packets[i]
            print(f"Packet No: {i} Packet Size: {packet_size}")
            if packet_size > self.bucket_size:
                print("Bucket Overflow")
            else:
                while packet_size > output_rate:
                    print(f"{output_rate} bytes sent")
                    packet_size -= output_rate

                if packet_size:
                    print(f"Last {packet_size} bytes sent")

                print("Bucket output Successful")


bucket_size = int(input("Enter the Bucket Size: "))
output_rate = int(input("Enter the output rate: "))
packets = [int(x) for x in input("Enter the input packets: ").split()]
lb = LeakyBucket(bucket_size, output_rate, packets)
lb.traffic_shaping()
