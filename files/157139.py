<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:07:55 PM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLUJSODJGRkw7MjU2OC0wNy0xNjswNTo1Njo0NCBQTTsyNzcx"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLUJSODJGRkw7MjU2OC0wNy0xNjswNjowNzo1NSBQTTsxOzI4Nzg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, year" type="Integer" array="False" size=""/>
            <declare name="in, y1, y2, y3" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="in"/>
            <assign variable="in" expression="in*0.01"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="y1" expression="money*(1+in)"/>
            <assign variable="y2" expression="y1*(1+in)"/>
            <assign variable="y3" expression="y2*(1+in)"/>
            <output expression="&quot;Year 1: &quot; &amp; y1" newline="True"/>
            <output expression="&quot;Year 2: &quot; &amp; y2" newline="True"/>
            <output expression="&quot;Year 3: &quot; &amp; y3" newline="True"/>
        </body>
    </function>
</flowgorithm>