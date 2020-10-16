<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>CSC561 | Lab1c</title>
  </head>
<body>

<h3>Status of all of our inventory items - (Inventory -> { belongsTo } -> Status)</h3>

<table border="1">
				<thead>
          <th>Inventory Item</th>
					<th>Description</th>
				</thead>

				<tbody>
					@foreach ($inventories as $inventory)
            <tr>
              <td>{{ $inventory->description }}</td>
							<td>{{ $inventory->status->description }}</td>
            </tr>
          @endforeach
        </tbody>
</table> 

<h3>Inventory Items that have a status of Checked Out - (Status -> { hasMany } -> Inventory)</h3>

<table border="1">
				<thead>
          <th>Inventory Item</th>
					<th>Description</th>
				</thead>

				<tbody>
					@foreach ($statuses->where('description', 'Checked Out ')->first()->inventory as $checked_out_inventory)
            <tr>
              <td>{{ $checked_out_inventory->description }}</td>
							<td>{{ $checked_out_inventory->status->description }}</td>
            </tr>
          @endforeach
        </tbody>
</table> 

<h3>Record of Items checked out by User1 - (Transaction -> { belongsTo } -> User)</h3>

<table border="1">
				<thead>
          <th>Inventory Item</th>
					<th>Checkout Time</th>
				</thead>

				<tbody>
					@foreach ($transactions->where('user_id', 1) as $transaction)
            <tr>
              <td>{{ $transaction->inventory->description }}</td>
							<td>{{ $transaction->checkout_time }}</td>
            </tr>
          @endforeach
        </tbody>
</table>

<h3>Record of Users checking items out before September 8, 2018 - (User -> { hasMany } -> Transactions)</h3>

<table border="1">
				<thead>
          <th>User First Name</th>
          <th>Inventory Item</th>
					<th>Checkout Time</th>
          <th>Status</th>
				</thead>

				<tbody>
					@foreach ($transactions->where('checkout_time', '<', '2018-08-03') as $transaction)
            <tr>
              <td>{{ $transaction->user->first_name }}</td>
							<td>{{ $transaction->inventory->description }}</td>
              <td>{{ $transaction->checkout_time }}</td>
              <td>{{ $transaction->inventory->status->description }}</td>
            </tr>
          @endforeach
        </tbody>
</table>

</body>
</html>
