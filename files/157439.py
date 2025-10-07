<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lap4_3"/>
        <attribute name="authors" value="sooth"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-19 11:20:02 AM"/>
        <attribute name="created" value="c29vdGg7QU9NU0lOTjsyMDI1LTA3LTE5OzExOjEyOjUyIEFNOzIzNTc="/>
        <attribute name="edited" value="c29vdGg7QU9NU0lOTjsyMDI1LTA3LTE5OzExOjIwOjAyIEFNOzI7MjQ2MA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="startnumber" type="Integer" array="False" size=""/>
            <declare name="endnumber" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="startnumber"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="endnumber"/>
            <while expression="startnumber&lt;=endnumber">
                <output expression="startnumber" newline="True"/>
                <assign variable="startnumber" expression="startnumber+1"/>
            </while>
        </body>
    </function>
</flowgorithm>