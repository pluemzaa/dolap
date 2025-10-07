<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_count"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 11:12:05 PM"/>
        <attribute name="created" value="VXNlcjsyNjc4Ny0zMjAxOzI1NjgtMDctMjA7MTE6MDk6MDMgUE07MjIxNg=="/>
        <attribute name="edited" value="VXNlcjsyNjc4Ny0zMjAxOzI1NjgtMDctMjA7MTE6MTI6MDUgUE07MTsyMzIw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, j" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="j"/>
            <while expression="i&lt;(j+1)">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>