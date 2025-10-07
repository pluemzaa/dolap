<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flow3.fl"/>
        <attribute name="authors" value="laila"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-21 06:11:05 PM"/>
        <attribute name="created" value="bGFpbGE7VEFUVEVQOzIwMjUtMDctMjE7MDU6NTY6NTcgUE07MjI3Mg=="/>
        <attribute name="edited" value="bGFpbGE7VEFUVEVQOzIwMjUtMDctMjE7MDY6MTE6MDUgUE07MTsyMzY1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="number, umber, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="number"/>
            <assign variable="i" expression="number"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="umber"/>
            <output expression="number" newline="True"/>
            <while expression="i&lt;umber">
                <assign variable="i" expression="i+1"/>
                <output expression="i" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>