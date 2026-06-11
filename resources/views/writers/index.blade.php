@extends('layouts.app')

@section('title', 'Writers')

@section('content')
<div class="row">
    <div class="col-12">
        <h1>писатели</h1>
        @if(session('success'))
            <div class="alert alert-success">
                {{ session('success') }}
            </div>
        @endif

        <table class="table table-striped">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>имя</th>
                    <th>др</th>
                    <th>создана запись</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                @forelse($writers as $writer)
                    <tr>
                        <td>{{ $writer->id }}</td>
                        <td>{{ $writer->name }}</td>
                        <td>{{ $writer->born ? $writer->born->format('Y-m-d') : 'N/A' }}</td>
                        <td>{{ $writer->created_at->format('Y-m-d H:i:s') }}</td>
                    </tr>
                @empty
                    <tr>
                        <td colspan="5" class="text-center">нет писателей</td>
                    </tr>
                @endforelse
            </tbody>
        </table>
    </div>
</div>
@endsection
