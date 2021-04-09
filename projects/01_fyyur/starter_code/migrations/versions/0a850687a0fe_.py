"""empty message

Revision ID: 0a850687a0fe
Revises: b72b4a8219e1
Create Date: 2021-04-07 14:53:32.866464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a850687a0fe'
down_revision = 'b72b4a8219e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_venue', sa.Boolean(), nullable=False),
    sa.Column('seeking_description', sa.String(), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=False),
    sa.Column('seeking_description', sa.String(), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('ArtistGenre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('artist_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['artist_name'], ['Artist.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('VenueGenre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('venue_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.ForeignKeyConstraint(['venue_name'], ['Venue.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.String(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id', 'venue_id', 'artist_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shows')
    op.drop_table('VenueGenre')
    op.drop_table('ArtistGenre')
    op.drop_table('Venue')
    op.drop_table('Artist')
    # ### end Alembic commands ###
