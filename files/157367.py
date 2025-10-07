<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_2"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 05:58:05 PM"/>
        <attribute name="created" value="VXNlcjsyNjc4Ny0zMjAxOzI1NjgtMDctMTk7MTI6NDI6NDUgUE07MjIyOA=="/>
        <attribute name="edited" value="VXNlcjsyNjc4Ny0zMjAxOzI1NjgtMDctMTk7MDU6NTg6MDUgUE07NDsyMzQ0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="CoffeeQty, TeaQty, menu, qty, price, quantity, total" type="Integer" array="False" size=""/>
            <assign variable="qty" expression="0"/>
            <assign variable="CoffeeQty" expression="10"/>
            <assign variable="TeaQty" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="menu==1">
                <then>
                    <if expression="quantity&lt;=CoffeeQty">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="price" expression="25*quantity"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                            <assign variable="price" expression="0"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu==2">
                        <then>
                            <if expression="quantity&gt;TeaQty">
                                <then/>
                                <else/>
                            </if>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Invalid menu selected&quot;" newline="True"/>
                        </else>
                    </if>
                    <assign variable="price" expression="0"/>
                </else>
            </if>
            <assign variable="total" expression="price"/>
            <output expression="&quot;Total price:&quot;&amp;total&amp; &quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>