<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Book extends Model
{
    use HasFactory;

    protected $fillable = [
        'writer_id',
        'name',
        'created_at',
    ];

    public function writer()
    {
        return $this->belongsTo(Writer::class);
    }
}
