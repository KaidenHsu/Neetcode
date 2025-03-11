class DynamicArray {
    private:
        int capacity;
        int length;
        int* arr;
    
    public:
        DynamicArray(int capacity) {
            this->capacity = capacity;
            length = 0;
            arr = new int[capacity];
        }
    
        int get(int i) {
            return arr[i];
        }
    
        void set(int i, int n) {
            arr[i] = n;
        }
    
        void pushback(int n) {
            if (length >= capacity)
                resize();
    
            arr[length++] = n;
        }
    
        int popback() {
            if (length <= 0)
                return -1;
    
            return arr[--length];
        }
    
        void resize() {
            int* new_arr = new int[2*capacity];
    
            for (int i = 0; i < length; i++)
                new_arr[i] = arr[i];
            
            delete[] arr;
            arr = new_arr;
            capacity *= 2;
        }
    
        int getSize() {
            return length;
        }
    
        int getCapacity() {
            return capacity;
        }
    };
    