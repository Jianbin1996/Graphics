module aa(
  logic clk,
  logic reset_n,
  logic [size-1: 0] frame [size-1:0],
  logic th,
  logic done
);
  
  

  logic [9:0] row, col;
  logic [size-1: 0] avg_frame [size-1:0],
  
  always @(posedge clk) begin 
    if (!reset_n) begin
        row = 1;
        col = 1;
    end else begin 
      if row <size-1 
        if col < size - 1 
          if (frame[row][col] > th && (frame[row][col] < th || frame[row][col] < th )  )
            avg_frame[row][col] <= (frame[row][col]+frame[row+1][col]+frane[row-1][col]+frame[row][col+1]+frame[row][col-1])>>4 //if it is a black pixel neighbours a white pixel
            //calculate the avg of the neighbouring pixels and divide by 4 
            row <= row +1;
            col <= col +1;
    
  end 
    
    assign done = (row == size-1 && col ==1)? 1 : 0; //assert done when the whole frame has been processed 
   
    endmodule 
